from django.utils.translation import ugettext_lazy as _

from cms.utils.permissions import get_model_permission_codename
from cms.wizards.wizard_pool import wizard_pool

from .cms_plugins import Alias
from .compat import CompatWizard
from .forms import CreateAliasWizardForm, CreateCategoryWizardForm
from .models import Alias as AliasModel, Category


class CreateAliasWizard(CompatWizard):

    def user_has_add_permission(self, user, **kwargs):
        return Alias.can_create_alias(user)


class CreateAliasCategoryWizard(CompatWizard):

    def user_has_add_permission(self, user, **kwargs):
        return user.has_perm(
            get_model_permission_codename(Category, 'add'),
        )


create_alias_wizard = CreateAliasWizard(
    title=_('New alias'),
    weight=200,
    form=CreateAliasWizardForm,
    model=AliasModel,
    description=_('Create a new alias.'),
    edit_mode_on_success=True,
)
create_alias_category_wizard = CreateAliasCategoryWizard(
    title=_('New alias category'),
    weight=200,
    form=CreateCategoryWizardForm,
    model=Category,
    description=_('Create a new alias category.'),
    edit_mode_on_success=True,
)

wizard_pool.register(create_alias_wizard)
wizard_pool.register(create_alias_category_wizard)
